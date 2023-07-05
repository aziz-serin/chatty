<script>
    export let symbol;
    export let bgColor;
</script>

<button on:click style="background-color: {bgColor}">
    {symbol}
</button>

<style>
    button {
        border: none;
        padding: 0.5rem 2rem;
        color: black;
        font-size: 1.0rem;
        border-radius: 1rem;
        transition: all 250ms;
        transform-origin: center;
        box-shadow: 0px 3px 3px rgba(0, 0, 0, 0.25),
        inset 0px -2px 3px rgba(0, 0, 0, 0.25);
        width: 100%;
    }
    button:hover {
        cursor: pointer;
        transform: scale(0.975);
        box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.25);
    }
</style>