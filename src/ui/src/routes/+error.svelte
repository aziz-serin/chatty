<script lang="ts">
  import { page } from "$app/stores";
  import { fade } from 'svelte/transition';
	import { afterUpdate } from "svelte";
</script>

<slot>
  <h1 transition:fade|global={{delay:100}}>
    {$page.status} {$page.error.message}
  </h1>
</slot>


<style>
  h1 {
      font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
      text-decoration: #424245;
      color: #424245;
      position: absolute;
      top: 40%;
      bottom: 40%;
      text-align: center;
      width: 100%;
      height: 100%;
  }
</style>