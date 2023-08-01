<script lang="ts">
  import { slide } from 'svelte/transition';
  import { fade } from 'svelte/transition';

  const CHAT: string = "chat";
  const PROMPT: string = "prompt";
  const TRANSCRIBE: string = "transcribe";
  const TO_SPEECH: string = "to speech";
  const TRANSLATE: string = "translate";
  const HISTORY: string = "history";

  let current = CHAT;

</script>

<svelte:head>
    <title>Chatty</title>
</svelte:head>

<slot>
  <div class="content">
    <h1 transition:slide class="headers" style="font-size: 50px">Chatty</h1>
    <p> A website designed to test out Chat-GPT features combined with text to speech APIs! Do you need help doing your
      homework or help you learn something new? Are you bored and you want to learn random facts? Do you need to
      translate or transcribe a given audio file? Do you want to create speech from a text you have in a variety of
      languages? Then, you are at the perfect place! You can do any of these thanks to this website, and if you host it
      locally or in a cloud platform of your choice, the cost of it will be the fraction of what OpenAI asks for their premium
      subscription, and in addition, you will have text to speech abilities!
    </p>
    <br>
    <ul class="list">
      <li class="listElement">
        <button on:click={() => {current = CHAT;}} class="buttons">
          {"Chat"}
        </button>
        <button on:click={() => {current = PROMPT;}} class="buttons">
          {"Prompt"}
        </button>
        <button on:click={() => {current = TRANSCRIBE;}} class="buttons">
          {"Transcribe"}
        </button>
        <button on:click={() => {current = TO_SPEECH;}} class="buttons">
          {"To Speech"}
        </button>
        <button on:click={() => {current = TRANSLATE;}} class="buttons">
          {"Translate"}
        </button>
        <button on:click={() => {current = HISTORY;}} class="buttons">
          {"History"}
        </button>
      </li>
    </ul>
    <br>
    <div class="information">
      {#if current === CHAT}
        <p transition:fade|global={{delay:100}}>
          <a href="/chat">Chat</a> tab allows you to communicate with Chat-GPT APIs using a context. This functionality can be associated
          with having a conversation with the AI model. Each message is considered as part of the ongoing conversation,
          and the chat model gives responses accordingly. The app will save your message history and configuration parameters
          and display them in the <a href="/history">History</a> tab for you to access later. You can configure the name of the conversation,
          chat model and token limit of the conversations.
        </p>
      {:else if current === PROMPT}
        <p transition:fade|global={{delay:100}}>
          <a href="/prompt">Prompt</a> tab allows you to communicate with Chat-GPT APIs without using a memory. There is no context of
          conversation for this functionality, each prompt is considered as an individual message. You can configure
          the chat model you use as well as the token limit for the given request.
        </p>
      {:else if current === TRANSCRIBE}
        <p transition:fade|global={{delay:100}}>
          <a href="/transcribe">Transcribe</a> tab allows you to communicate with OpenAI's speech to text api to convert any audio file you have
          into text. You can configure the speech to text model to use different models. Supported formats of audio are:
          ."mp4, .mp3, .mpeg, .mpga, .m4a, .wav, .webm".
        </p>
      {:else if current === TO_SPEECH}
        <p transition:fade|global={{delay:100}}>
          <a href="/speech">To Speech</a> tab allows you to convert a given piece of text into speech by using Google's text to speech apis. You can
          configure the language and the sex of the speaker for this functionality. Upon sending the text message, the audio file is automatically downloaded.
        </p>
      {:else if current === TRANSLATE}
        <p transition:fade|global={{delay:100}}>
          <a href="/translate">Translate</a> tab allows you to communicate with OpenAI's speech to text api to convert any audio file you have
          into text and translate to English. At the moment, OpenAI only supports translation to english from other languages. You can configure
          the speech to text model to use different models. Supported formats of audio are: ."mp4, .mp3, .mpeg, .mpga, .m4a, .wav, .webm".
        </p>
      {:else if current === HISTORY}
        <p transition:fade|global={{delay:100}}>
          <a href="/history">History</a> tab allows you to view your previous <a href="/chat">Chat</a> histories. You can access them and continue your
          conversation using this tab. You can also delete previous conversations.
        </p>
      {/if}
    </div>

    <div class="footer">
      <p style="text-align: center">Author: <a href="https://github.com/aziz-serin" class="author">Aziz Serin</a></p>
    </div>
  </div>
</slot>

<style>
  .content {
    position: absolute;
    top:5%;
    font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
    left: 15%;
    right: 15%;
    height: 80%;
  }

  .headers {
    color: #424245;
  }

  .list {
    font-size: 15px;
    list-style: none;
    text-align: center;
  }

  button {
      border: none;
      padding: 0.5rem 2rem;
      color: black;
      font-size: 18px;
      border-radius: 1rem;
      transition: all 250ms;
      transform-origin: center;
      box-shadow: 0px 3px 3px rgba(0, 0, 0, 0.25),
      inset 0px -2px 3px rgba(0, 0, 0, 0.25);
      width: 12%;
      background-color: gray;
      margin: 10px;
      text-overflow: clip;
    }
    button:hover {
      cursor: pointer;
      transform: scale(0.975);
      box-shadow: 0px 1px 3px rgba(0, 0, 0, 0.25);
    }

    p {
      font-size: 18px;
    }

    a {
      text-decoration: none;
      color: black;
      font-size: 22px;
    }
    a:hover {
      box-shadow: gray;
      color: gray;
    }

    .author {
      text-decoration: none;
      color: white;
      font-size: 18px;
    }

    .footer {
        text-align: center;
        font-family: "Helvetica Neue", "Helvetica", "Arial", sans-serif;
        font-size: 15px;
        position: fixed;
        width: 70%;
        background-color: #424245;
        color: white;
        bottom: 0;
    }
</style>