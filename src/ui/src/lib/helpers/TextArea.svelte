<script lang="js">
	import {autoHeight} from "svelte-textarea-auto-height";
	export let value = '';
  export let placeHolder = '';
	export let readonly = false;

</script>

<div class="container">
	{#if readonly}
		<textarea bind:value use:autoHeight placeholder={placeHolder} readonly class="readonlyTextArea"></textarea>
	{:else}
		<textarea bind:value use:autoHeight placeholder={placeHolder} class="inputTextArea"></textarea>
	{/if}

</div>

<style>
	.container {
		position: relative;
	}

	textarea {
		font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
		padding: 0.5em;
		box-sizing: border-box;
		line-height: 1.2;
		overflow-y: scroll;
		min-height: 100px;
		max-height: 150px;
		resize: none;
		background: white;
		border: 1px solid gray;
		color: black;
		width: 100%;
		font-size: 16px;
	}

	textarea::placeholder {
  	color: black;
	}

	textarea:focus {
		outline: none !important;
    border:1px solid gray;
    box-shadow: 0 0 10px gray;
	}

	.readonlyTextArea {
		border: transparent;
	}

	.inputTextArea {
		border: 1px solid gray;
	}
</style>