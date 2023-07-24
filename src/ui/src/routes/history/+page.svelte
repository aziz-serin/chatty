<script lang="ts">
  import HistoryFrame from "$lib/components/HistoryFrame.svelte";
  import { getAllContext } from "./historyAPIFetch";
  import { onMount } from "svelte";

  let context_id = [];
  let stt_model = [];
  let chat_model = [];
  let token_limit = [];

  onMount(async() => {
    const response = await getAllContext();
    response.forEach((data) => {
      context_id.push(data["_id"]);
      stt_model.push(data["stt_model"]);
      chat_model.push(data["chat_model"]);
      token_limit.push(data["token_limit"]);
    })
    context_id = context_id;
    stt_model = stt_model;
    chat_model = chat_model;
    token_limit = token_limit;
  });
</script>

<slot>
  {#if context_id.length === 0}
    <p class="loading">Loading ....</p>
  {:else}
    <HistoryFrame
      labels={context_id}
      chat_models={chat_model}
      token_limits={token_limit}
      stt_models={stt_model}
    >
    </HistoryFrame>
  {/if}
</slot>

<style>
  .loading {
    position: absolute;
    top: 5%;
    font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  }
</style>