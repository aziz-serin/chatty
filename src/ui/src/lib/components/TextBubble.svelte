<script lang="ts">
  export let sender = "user";
  export let text = "";
</script>

{#if sender === "user"}
  <div class="talk-bubble tri-right round btm-right-in">
    <div class="talktext">
      <p> {text} </p>
    </div>
  </div>
{:else}
  <div class="talk-bubble tri-right round btm-left-in" >
    <div class="talktext">
      <p> {text} </p>
    </div>
  </div>
{/if}


<style>

  /* CSS talk bubble */
  .talk-bubble {
    margin: 10px;
    font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
    display: inline-block;
    position: relative;
    width: 50%;
    height: auto;
    background-color: lightgray;
  }

  .round{
    border-radius: 30px;
    -webkit-border-radius: 30px;
    -moz-border-radius: 30px;

  }

  /* Right triangle placed top left flush. */
  .tri-right.border.left-top:before {
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: -40px;
    right: auto;
    top: -8px;
    bottom: auto;
    border: 32px solid;
    border-color: #666 transparent transparent transparent;
  }
  .tri-right.left-top:after{
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: -20px;
    right: auto;
    top: 0;
    bottom: auto;
    border: 22px solid;
    border-color: lightgray transparent transparent transparent;
  }

  /* Right triangle, left side slightly down */
  .tri-right.border.left-in:before {
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: -40px;
    right: auto;
    top: 30px;
    bottom: auto;
    border: 20px solid;
    border-color: #666 #666 transparent transparent;
  }
  .tri-right.left-in:after{
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: -20px;
    right: auto;
    top: 38px;
    bottom: auto;
    border: 12px solid;
    border-color: lightgray lightgray transparent transparent;
  }

  /*Right triangle, placed bottom left side slightly in*/
  .tri-right.border.btm-left:before {
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: -8px;
    right: auto;
    top: auto;
    bottom: -40px;
    border: 32px solid;
    border-color: transparent transparent transparent #666;
  }
  .tri-right.btm-left:after{
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: 0;
    right: auto;
    top: auto;
    bottom: -20px;
    border: 22px solid;
    border-color: transparent transparent transparent lightgray;
  }

  /*Right triangle, placed bottom left side slightly in*/
  .tri-right.border.btm-left-in:before {
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: 30px;
    right: auto;
    top: auto;
    bottom: -40px;
    border: 20px solid;
    border-color: #666 transparent transparent #666;
  }
  .tri-right.btm-left-in:after{
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: 38px;
    right: auto;
    top: auto;
    bottom: -20px;
    border: 12px solid;
    border-color: lightgray transparent transparent lightgray;
  }

  /*Right triangle, placed bottom right side slightly in*/
  .tri-right.border.btm-right-in:before {
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: auto;
    right: 30px;
    bottom: -40px;
    border: 20px solid;
    border-color: #666 #666 transparent transparent;
  }
  .tri-right.btm-right-in:after{
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: auto;
    right: 38px;
    bottom: -20px;
    border: 12px solid;
    border-color: lightgray lightgray transparent transparent;
  }

  .tri-right.border.btm-right:before {
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: auto;
    right: -8px;
    bottom: -40px;
    border: 20px solid;
    border-color: #666 #666 transparent transparent;
  }
  .tri-right.btm-right:after{
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: auto;
    right: 0;
    bottom: -20px;
    border: 12px solid;
    border-color: lightgray lightgray transparent transparent;
  }

  /* Right triangle, right side slightly down*/
  .tri-right.border.right-in:before {
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: auto;
    right: -40px;
    top: 30px;
    bottom: auto;
    border: 20px solid;
    border-color: #666 transparent transparent #666;
  }
  .tri-right.right-in:after{
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: auto;
    right: -20px;
    top: 38px;
    bottom: auto;
    border: 12px solid;
    border-color: lightgray transparent transparent lightgray;
  }

  /* Right triangle placed top right flush. */
  .tri-right.border.right-top:before {
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: auto;
    right: -40px;
    top: -8px;
    bottom: auto;
    border: 32px solid;
    border-color: #666 transparent transparent transparent;
  }
  .tri-right.right-top:after {
    content: ' ';
    position: absolute;
    width: 0;
    height: 0;
    left: auto;
    right: -20px;
    top: 0;
    bottom: auto;
    border: 20px solid;
    border-color: lightgray transparent transparent transparent;
  }

  /* talk bubble contents */
  .talktext {
    padding: 1em;
    text-align: left;
    line-height: 1.5em;
    -webkit-margin-before: 0;
    -webkit-margin-after: 0;
    top: 0;
    min-height: 50px;
    overflow: hidden;
  }

  p {
    background: transparent;
  }
</style>