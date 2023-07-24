export class Message {
	public sender: string;
	public msg: string;
		constructor(sender: string, msg: string) {
			this.sender = sender;
			this.msg = msg;
		}
	}

export async function delete_context(context_id: string) {
	const url: string = 'http://chatty.localtest.me:5005/api/context' + "?context_id=" + context_id;
		const response: Response = await fetch(url, {
			method: 'DELETE',
		});
	return response.ok;
}