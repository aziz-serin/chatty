<script lang="js">
  import ChatBox from "$lib/components/ChatBox.svelte";
	import SubmitButton from "$lib/components/SubmitButton.svelte";
	import TextBubble from "$lib/components/TextBubble.svelte";
	import ConfigInput from "$lib/components/ConfigInput.svelte";
	import { fade } from 'svelte/transition';
	import { afterUpdate } from "svelte";
	import { sendChat } from "./promptAPIFetch.ts";

	let message = "";
	let messages = [];
	let element;
	let chatModelValue = "gpt-3.5-turbo";
	let tokenCount = 4000;

	const configInputs = {
		"CHATGPT MODEL": chatModelValue,
		"TOKEN COUNT": tokenCount
	}

	class Message {
		constructor(sender, msg) {
			this.sender = sender;
			this.msg = msg;
		}
	}

	function saveUserMessage(userMessage) {
		const msg = new Message("user", userMessage);
		messages.push(msg);
		messages = messages;
	}

	async function chat(userMessage) {
		message = "";
		const response = await sendChat({
			"prompt": userMessage,
			"model": chatModelValue,
			"token_limit": tokenCount
		});
		let responseTokenCount = response["token_count"];
		let responseMessage = response["message"];
		const repliedMessage = new Message("replied", responseMessage);
		messages.push(repliedMessage);
		messages = messages;
	}

	async function sendUserMessage() {
		saveUserMessage(message);
		await chat(message);
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
		<!--CONFIG_SIDEBAR-->
		<div class="configContainer" transition:fade|global={{delay:100}}>
			{#each Object.entries(configInputs) as [key, value]}
				<form class="configSection">
					<ConfigInput
						bind:inputValue={value}
						label={key}
					>
					</ConfigInput>
				</form>
			{/each}
		</div>
		<!--MESSAGES-->
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
	<!--SUBMISSION-->
	<div class="submission" transition:fade|global={{delay:100}}>
			<div class="chatBox">
				<ChatBox bind:message></ChatBox>
			</div>
			<div class="submit">
				<SubmitButton on:click={sendUserMessage} symbol={"✉️"} bgColor={"rgba(0, 0, 0, 0.8)"}></SubmitButton>
			</div>
	</div>

</slot>

<style>
	.configContainer {
		position: absolute;
		height: 96.2%;
		background-color: #424245;
		left: 0;
		bottom: 0;
		top: 45px;
		width: 18%;
		z-index: 990;
	}

	.configSection {
		background: transparent;
		position: relative;
		height: 7%;
		margin: 10px;
		z-index: 999;
	}

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
