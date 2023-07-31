<script lang="js">
  export let label = ""
  export let inputValue = "";
  export let options = [];
</script>

<div class="labelContainer overlay">
  <label>{label}</label>
</div>
<div class="inputContainer overlay">
  <select bind:value={ inputValue }>
    {#each options as option}
      <option value={ option }>
        { option }
      </option>
    {/each}
  </select>
</div>

<style>
  select {
    font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;;
    background-color: transparent;
    color: white;
    left: 0;
    border-color: white;
    text-align: center;
    font-size: 16px;
    width: 95%;
  }

  input:focus {
		outline: none !important;
    border:1px solid white;
    box-shadow: 0 0 10px white;
	}

  .inputContainer {
    position: relative;
    bottom: 0;
    margin-top: 20px;
    width: 100%;
    height: 80px;
  }

  label {
    font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;;
    color: white;
    font-size: 18px;
    overflow-x: hidden;
    overflow-y: hidden;
  }

  .labelContainer {
    position: relative;
    width: 100%;
    height: 5px;
    left: 0;
    margin-bottom: 10%;
    background-color: transparent;
  }

  .overlay {
    z-index: 9;
  }
</style>