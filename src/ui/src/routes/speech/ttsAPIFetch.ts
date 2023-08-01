import {selectVoiceFromOptions} from "$lib/helpers/voices";
import {HOST_NAME} from "$lib/helpers/constants";

export async function tts(variables: { text: string; language: string; gender: string }) {
    const voiceName = selectVoiceFromOptions(variables.language, variables.gender)
    return await fetch(`${HOST_NAME}/api/tts`, {
        method: 'POST',
        body: JSON.stringify({
            text: variables.text,
            voice_name: voiceName
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    });
}
