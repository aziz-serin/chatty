<script lang="ts">
  import ChatBox from "$lib/components/ChatBox.svelte";
	import SubmitButton from "$lib/components/SubmitButton.svelte";
	import TextBubble from "$lib/components/TextBubble.svelte";
	import ConfigDropdown from "$lib/components/ConfigDropdown.svelte";
	import { fade } from 'svelte/transition';
	import { afterUpdate } from "svelte";
	import { tts } from "./ttsAPIFetch";
	import {languages} from "$lib/helpers/voices";

	let message = "";
	let messages = [];
	let element;
	let language = "English";
	let gender = "Female";

	function saveUserMessage(userMessage) {
		messages.push(userMessage);
		messages = messages;
	}

	async function tts_sender(userMessage: string) {
		message = "";
		const response = await tts({
			"text": userMessage,
			"language": language,
			"gender": gender,
		});
		const blob = await response.blob();
		const url = URL.createObjectURL(blob);
		const media = document.createElement('a');
		media.style.display = "none";
		media.setAttribute("download", "media.m4a");
		document.body.appendChild(media);
		media.href = url;
		media.click();
		URL.revokeObjectURL(url);
	}

	async function sendText() {
		saveUserMessage(message);
		await tts_sender(message);
	}

	afterUpdate(() => {
		if(messages) scrollToBottom(element);
  });

	const scrollToBottom = async (node) => {
    node.scroll({ top: node.scrollHeight, behavior: 'smooth' });
  };

</script>

<svelte:head>
    <title>{`To Speech`}</title>
</svelte:head>

<slot>
	<div>
		<!--CONFIG_SIDEBAR-->
		<div class="configContainer" transition:fade|global={{delay:100}}>
			<form class="configSection">
				<ConfigDropdown
					bind:inputValue={language}
					options={languages}
					label={"Language"}
				>
				</ConfigDropdown>
			</form>
			<form class="configSection">
				<ConfigDropdown
					bind:inputValue={gender}
					options={["Male", "Female"]}
					label={"Sex"}
				>
				</ConfigDropdown>
			</form>
		</div>
		<!--MESSAGES-->
		<div bind:this={element} class="messages">
			{#each messages as msg}
        <div class="list" transition:fade|global={{delay:100}}>
          <TextBubble sender={"Stt"} text={msg}></TextBubble>
        </div>
			{/each}
		</div>
	</div>
	<!--SUBMISSION-->
	<div class="submission" transition:fade|global={{delay:100}}>
			<div class="chatBox">
				<ChatBox bind:message></ChatBox>
			</div>
			<div class="submit">
				<SubmitButton on:click={sendText} symbol={"✉️"} bgColor={"rgba(0, 0, 0, 0.8)"}></SubmitButton>
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
		left: 10%;
		height: 80%;
		max-height: 80%;
		right:0.5%;
		text-align: center;
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