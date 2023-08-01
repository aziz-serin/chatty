import {HOST_NAME} from "$lib/helpers/constants";

export class Message {
	public sender: string;
	public msg: string;
		constructor(sender: string, msg: string) {
			this.sender = sender;
			this.msg = msg;
		}
	}

export async function delete_context(context_id: string) {
	const response: Response = await fetch(`${HOST_NAME}/api/context?context_id=${context_id}`, {
		method: 'DELETE',
	});
	return response.ok;
}

export async function get_context(context_id: string) {
	const response: Response = await fetch(`${HOST_NAME}/api/context?context_id=${context_id}`, {
		method: 'GET'
	});
	if (response.ok) {
		return await response.json();
	}
	return [];
}

export async function transcribeAudioFile(file: File, stt_model: string) {
	let formData = new FormData();
	formData.append('file', file);
	formData.append('stt_model', stt_model);
	const response: Response = await fetch(`${HOST_NAME}/api/stt?method=transcribe`, {
		method: 'POST',
		body: formData
	});
	const data = await response.json();
	return data["response"];
}

export async function translateAudioFile(file: File, stt_model: string) {
	let formData = new FormData();
	formData.append('file', file);
	formData.append('stt_model', stt_model);
	const response: Response = await fetch(`${HOST_NAME}/api/stt?method=translate`, {
		method: 'POST',
		body: formData
	});
	const data = await response.json();
	return data["response"];
}