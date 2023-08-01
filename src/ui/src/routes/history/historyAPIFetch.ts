import {HOST_NAME} from "$lib/helpers/constants";

export async function getAllContext(){
    const response = await fetch(`${HOST_NAME}/api/context?isAll=true`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    return await response.json();
}