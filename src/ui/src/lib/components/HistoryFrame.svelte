<script lang="ts">
  import SubmitButton from "$lib/components/SubmitButton.svelte";
  import { fade } from 'svelte/transition';
  import { delete_context } from "$lib/helpers/scripts";

  export let labels = [];
  export let chat_models = [];
  export let token_limits = [];
  export let stt_models = [];
</script>

<table class="frame" bind:this={labels}>
  <tr transition:fade|global={{delay:100}}>
    <th>Context ID</th>
    <th>Chat Model</th>
    <th>Token Limit</th>
    <th>Speech to Text Model</th>
  </tr>
  {#each labels as label, i}
    <tr transition:fade|global={{delay:100 + (i+1)*100}}>
      <td class="hasBackground">
        <a href={'/chat?context_id=' + label}>
          {label}
        </a>
      </td>
      <td class="hasBackground">
        {chat_models[i]}
      </td>
      <td class="hasBackground">
        {token_limits[i]}
      </td>
      <td class="hasBackground">
        {stt_models[i]}
      </td>
      <td>
        <SubmitButton
          bgColor="lightcoral"
          symbol="Delete"
          on:click={delete_context(label)}
        >
        </SubmitButton>
      </td>
    </tr>
  {/each}
</table>

<style>
  a {
      text-decoration: none;
      color: black;
  }
  a:hover {
      box-shadow: gray;
      color: gray;
  }
  table {
    font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
  }
  .frame {
      position: absolute;
      height: 60px;
      width: 99%;
      top: 5%;
  }
  th {
    font-size: 22px;
    margin-bottom: 10px;
  }
  td {
    text-align: center;
    font-size: 18px;
    padding: 5px;
  }
  .hasBackground {
      background-color: lightgray;
  }

  table {
      border-spacing: 0.5em;
  }
</style>