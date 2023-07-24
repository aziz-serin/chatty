/** @type {import('./$types').PageLoad} */
export async function sendChat(variables: { token_limit: number; model: string; prompt: string;
    context_id: string; }){
    let context: string = variables.context_id;
    let exists: boolean = await contextExists(context);
    let body;
    if (!exists) {
        body = JSON.stringify({
            prompt: variables.prompt,
        });
    } else {
        body = JSON.stringify({
            prompt: variables.prompt,
            context_id: context
        });
    }
    const response: Response = await fetch('http://chatty.localtest.me:5005/api/conversation', {
        method: 'POST',
        body: body,
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
    const url: string = 'http://chatty.localtest.me:5005/api/context' + "?context_id=" + context_id;
    const response: Response = await fetch(url, {
        method: 'GET',
    });
    return response.ok;
}
