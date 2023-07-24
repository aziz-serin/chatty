/** @type {import('./$types').PageLoad} */
export async function getAllContext(){
    const response = await fetch('http://chatty.localtest.me:5005/api/context?isAll=true', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    return await response.json();
}