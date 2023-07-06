<script lang="js">
  import TextArea from "../helpers/TextArea.svelte";
  import SubmitButton from "$lib/components/SubmitButton.svelte";

  export let message = "";
  export let readonly = false;
</script>


<TextArea
  bind:value={message}
  readonly={readonly}
  placeHolder={"Enter your message here..."}
 />