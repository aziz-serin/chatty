<script lang="js">
  import NavBar from "$lib/components/NavBar.svelte";
</script>

<NavBar></NavBar>

<slot/>

<style>
  :global(body) {
      background-color: gray;
  }

</style>
