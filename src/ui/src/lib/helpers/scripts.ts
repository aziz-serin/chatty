export class Message {
	public sender: string;
	public msg: string;
		constructor(sender: string, msg: string) {
			this.sender = sender;
			this.msg = msg;
		}
	}