<script lang="js">
  import NavBar from "$lib/components/NavBar.svelte";
</script>

<NavBar></NavBar>

<svelte:head>
  <link rel="icon" type="image/x-icon" href="/assets/favicon.ico">
  <meta name="author" content="Aziz Serin">
  <meta name="chatty" content="noindex nofollow"/>
  <meta name="description" content="Playground application to experiment with Chat-GPT and Google's TTS APIs">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta charset="utf-8">
</svelte:head>

<slot/>

<style>
  :global(body) {
    background-color: white;
  }
</style>
