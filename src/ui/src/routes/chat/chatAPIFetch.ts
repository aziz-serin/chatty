import {HOST_NAME} from "$lib/helpers/constants";

export async function sendChat(variables: {
        token_limit: number;
        model: string;
        context_id: string;
        config: { chat_name: string };
        prompt: string
    }){
    let context: string = variables.context_id;
    let exists: boolean = await contextExists(context);
    if (!exists) {
        context = await createContext({
            token_limit: variables.token_limit,
            chat_model: variables.model,
            config: variables.config
        });
    }
    const response: Response = await fetch(`${HOST_NAME}/api/conversation`, {
        method: 'POST',
        body: JSON.stringify({
            prompt: variables.prompt,
            context_id: context
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();
    return {
        "message": data["response"],
        "token_count": data["token_count"],
        "context_id": data["context_id"]
    };
}

async function contextExists(context_id: string) {
    const url: string = `${HOST_NAME}/api/context` + "?context_id=" + context_id;
    const response: Response = await fetch(url, {
        method: 'GET',
    });
    return response.ok;
}

async function createContext(variables: {
        token_limit: number;
        chat_model: string;
        config: { chat_name: string };
    }) {
    const response: Response = await fetch(`${HOST_NAME}/api/context`, {
        method: 'POST',
        body: JSON.stringify({
            token_limit: variables.token_limit,
            chat_model: variables.chat_model,
            config: variables.config,
            stt_model: "whisper-1"
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();
    return data["context_id"];
}