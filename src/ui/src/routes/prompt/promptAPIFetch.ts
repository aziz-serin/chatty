/** @type {import('./$types').PageLoad} */
export async function sendPrompt(variables: { token_limit: number; model: string; prompt: string }){
    const response = await fetch('http://chatty.localtest.me:5005/api/chat', {
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
