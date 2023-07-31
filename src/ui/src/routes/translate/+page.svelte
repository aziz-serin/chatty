<script lang="ts">
	import SubmitButton from "$lib/components/SubmitButton.svelte";
	import TextBubble from "$lib/components/TextBubble.svelte";
	import ConfigInput from "$lib/components/ConfigInput.svelte";
	import { fade } from 'svelte/transition';
	import { afterUpdate } from "svelte";
	import { translateAudioFile } from "$lib/helpers/scripts";

	let files = [];
	let messages = [];
	let element;
	let sttModel = "whisper-1";
	let operationCount = 0;

	afterUpdate(() => {
		if(messages) scrollToBottom(element);
	});

	const scrollToBottom = async (node) => {
		node.scroll({ top: node.scrollHeight, behavior: 'smooth' });
	};

	async function sendAudioFile() {
		if (operationCount === 0) {
			alert('Currently the only supported translation language is from any language to English');
		}
		operationCount++;
		if (files.length === 0) {
			return;
		}
		console.log(files);
		const text = await translateAudioFile(files[0], sttModel);
		messages.push(text);
		messages = messages;
		files = [];
	}

</script>

<slot>
	<div>
		<!--CONFIG_SIDEBAR-->
		<div class="configContainer" transition:fade|global={{delay:100}}>
			<form class="configSection">
				<ConfigInput
					bind:inputValue={sttModel}
					label={"Speech To Text Model"}
				>
				</ConfigInput>
			</form>
		</div>
		<!--MESSAGES-->
		<div bind:this={element} class="messages">
			{#each messages as msg}
        <div class="list" transition:fade|global={{delay:100}}>
          <TextBubble sender={"Transcriber"} text={msg}></TextBubble>
        </div>
			{/each}
		</div>
	</div>
	<!--SUBMISSION-->
	<div class="submission" transition:fade|global={{delay:100}}>
      <div class="upload">
        <label class="inputLabel">
          Upload your audio file:
        </label>
        <input accept=".mp4, .mp3, .mpeg, .mpga, .m4a, .wav, .webm"
               type="file" bind:files class="fileInput"/>
      </div>
			<div class="submit">
				<SubmitButton on:click={sendAudioFile} symbol={"✉️"} bgColor={"rgba(0, 0, 0, 0.8)"}></SubmitButton>
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

  .upload {
    font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
    font-size: 20px;
    text-align: center;
    padding-bottom: 10px;
  }

	.submit {
		position: relative;
		text-align: center;
		background-color: transparent;
		width: 99%;
		right: 0.4%;
	}

  .fileInput {
    border: none;
    padding: 0.5rem 2rem;
    color: black;
    font-size: 1.0rem;
    border-radius: 1rem;
    transition: all 250ms;
    transform-origin: center;
    width: 60%;
    background-color: gray;
  }

	.fileInput:hover {
			cursor: pointer;
			transform: scale(0.995);
    }

  ::-webkit-file-upload-button {
    display: none;
  }

	.list {
		list-style: none;
    text-align: center;
	}
</style>