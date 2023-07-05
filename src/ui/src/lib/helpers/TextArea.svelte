<script lang="ts">
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
		overflow: scroll;
		min-height: 100px;
		resize: none;
		background: transparent;
		width: 100%;
		font-size: 16px;
	}

	textarea:focus {
		outline: none !important;
    border:1px solid rgba(0, 0, 0, 0.8);
    box-shadow: 0 0 10px gray;
	}

	.readonlyTextArea {
		border: transparent;
	}

	.inputTextArea {
		border: 1px solid gray;
	}
</style>