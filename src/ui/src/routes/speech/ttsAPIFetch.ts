import {selectVoiceFromOptions} from "$lib/helpers/voices";

export async function tts(variables: { text: string; language: string; gender: string }) {
    const voiceName = selectVoiceFromOptions(variables.language, variables.gender)
    return await fetch('http://chatty.localtest.me:5005/api/tts', {
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
