<script lang="ts">
  import ChatBox from "$lib/components/ChatBox.svelte";
	import SubmitButton from "$lib/components/SubmitButton.svelte";
	import TextBubble from "$lib/components/TextBubble.svelte";
	import ConfigInput from "$lib/components/ConfigInput.svelte";
  import { Message } from "$lib/helpers/scripts";
	import { fade } from 'svelte/transition';
	import { afterUpdate } from "svelte";
	import { sendChat } from "./chatAPIFetch";
  import { page } from "$app/stores";
	import {get_context} from "$lib/helpers/scripts";

	let message = "";
	let messages = [];
	let element;
  let context_id = "999";
	let chatModel =  "gpt-3.5-turbo";
	let tokenLimit =  4000;
	let chatName =  "Default";

  if ($page.url.searchParams.has("context_id")) {
      context_id = $page.url.searchParams.get("context_id");
			updateMessagesWithContext();
  }

	function saveUserMessage(userMessage) {
		messages.push(new Message("user", userMessage));
		messages = messages;
	}

	async function updateMessagesWithContext() {
		const context = await get_context(context_id);
		if (context["messages"].length === 0) {
			return;
		}
		context["messages"].forEach((value) => {
			switch (value["role"]) {
				case "user":
					messages.push(new Message("user", value["content"]));
					break;
				case "assistant":
					messages.push(new Message("replied", value["content"]));
					break;
				default:
					break;
			}
		});
		chatName = context["config"]["chat_name"];
		messages = messages;
	}

	async function chat(userMessage: string) {
		message = "";
		const response = await sendChat({
			"config": {"chat_name": chatName},
			"prompt": userMessage,
			"model": chatModel,
			"token_limit": tokenLimit,
      "context_id": context_id
    });
		let responseTokenCount = response["token_count"];
		let responseMessage = response["message"];
    if (context_id !== response["context_id"]) {
      context_id = response["context_id"]
      $page.url.searchParams.set("context_id", context_id)
    }
		messages.push(new Message("replied", responseMessage));
		messages = messages;
	}

	async function sendUserMessage() {
		saveUserMessage(message);
		console.log(chatName);
		await chat(message);
	}

	afterUpdate(() => {
		if(messages) scrollToBottom(element);
  });

	const scrollToBottom = async (node) => {
    node.scroll({ top: node.scrollHeight, behavior: 'smooth' });
  };

</script>

<svelte:head>
    <title>{`Chat`}</title>
</svelte:head>

<slot>
	<div>
		<!--CONFIG_SIDEBAR-->
		<div class="configContainer" transition:fade|global={{delay:100}}>
			<form class="configSection">
				<ConfigInput
					bind:inputValue={chatName}
					label={"Chat Name"}
				>
				</ConfigInput>
			</form>
			<form class="configSection">
				<ConfigInput
					bind:inputValue={chatModel}
					label={"Chat Model"}
				>
				</ConfigInput>
			</form>
			<form class="configSection">
				<ConfigInput
					bind:inputValue={tokenLimit}
					label={tokenLimit}
				>
				</ConfigInput>
			</form>
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
		margin: 20px;
		padding-bottom: 10px;
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