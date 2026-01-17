<script>
  export let data;
  const puzzle = data.puzzle;
</script>

{#if puzzle}
  <div class="page">
    <header class="header">
      <h1 class="title">{puzzle.title}</h1>
      <p class="subtitle">{puzzle.date}</p>
    </header>

    <main class="grid">
      {#each puzzle.answers as answer, index}
        <section class={`card level-${answer.level}`}>
          <h2 class="group-name">{answer.group}</h2>
          <ul class="members">
            {#each answer.members as member}
              <li class="member">{member}</li>
            {/each}
          </ul>
        </section>
      {/each}
    </main>
  </div>
{:else}
  <p class="empty">No puzzle loaded.</p>
{/if}
