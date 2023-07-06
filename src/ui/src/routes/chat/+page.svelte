<script lang="js">
  import ChatBox from "$lib/components/ChatBox.svelte";
	import SubmitButton from "$lib/components/SubmitButton.svelte";
	import TextBubble from "$lib/components/TextBubble.svelte";
	import SideBar from "$lib/components/SideBar.svelte";
	import { fade } from 'svelte/transition';
	import {afterUpdate} from "svelte";

	let message = "";
	let messages = [];
	let element;

	class Message {
		constructor(sender, msg) {
			this.sender = sender;
			this.msg = msg;
		}
	}

	function sendUserMessage() {
		let msg = new Message("user", message);
		messages.push(msg);
		let msg2 = new Message("replied", message);
		messages.push(msg2);
		messages = messages;
		message = "";
	}

	afterUpdate(() => {
		if(messages) scrollToBottom(element);
  });

	const scrollToBottom = async (node) => {
    node.scroll({ top: node.scrollHeight, behavior: 'smooth' });
  };

</script>

<slot>
	<div>
		<SideBar></SideBar>
		<div bind:this={element} class="messages">
			{#each messages as msg}
				{#if msg.sender === "user"}
					<div class="list user" transition:fade|global={{delay:100}}>
						<TextBubble sender={msg.sender} text={msg.msg}></TextBubble >
					</div>
				{:else}
					<div class="list replied" transition:fade|global={{delay:100}}>
						<TextBubble sender={msg.sender} text={msg.msg}></TextBubble>
					</div>
				{/if}
			{/each}
		</div>
	</div>
	<div class="submission">
			<div class="chatBox">
				<ChatBox bind:message></ChatBox>
			</div>
			<div class="submit">
				<SubmitButton on:click={sendUserMessage} symbol={"✉️"} bgColor={"rgba(0, 0, 0, 0.8)"}></SubmitButton>
			</div>
	</div>

</slot>

<style>

	.messages {
		overflow: hidden;
		overflow-y: scroll;
		position: fixed;
		bottom: 20%;
		top: 7%;
		width: 100%;
		height: 80%;
		max-height: 80%;
		right:0.5%;
	}

	.submission {
		background-color: transparent;
		position: absolute;
		bottom: 20px;
		width: 80%;
		left: 20%;
	}

	.chatBox {
		position: relative;
		bottom: 0;
		text-align: center;
		width: 99%;
		right: 0.4%;
	}

	.submit {
		position: relative;
		text-align: center;
		background-color: transparent;
		width: 99%;
		right: 0.4%;
	}

	.list {
		list-style: none;
	}

	.user {
		text-align: right;
	}

	.replied {
		text-align: left;
		margin-left: 20%;
	}
</style>
