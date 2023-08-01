import {HOST_NAME} from "$lib/helpers/constants";

export async function sendPrompt(variables: { token_limit: number; model: string; prompt: string }){
    const response = await fetch(`${HOST_NAME}/api/chat`, {
        method: 'POST',
        body: JSON.stringify(variables),
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();
    return {
        "message": data["response"],
        "token_count": data["token_count"]
    };
}
