<script lang="ts">
  import TextArea from "../helpers/TextArea.svelte";
  import SubmitButton from "$lib/components/SubmitButton.svelte";

  export let message: string = "";
  export let readonly: boolean = false;
</script>


<TextArea
  bind:value={message}
  readonly={readonly}
  placeHolder={"Enter your message here..."}
 />