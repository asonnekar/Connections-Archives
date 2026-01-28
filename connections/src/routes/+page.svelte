<script lang="ts">
  import '../app.css';
  export let data: { puzzle: { title: string; answers: { level: number; members: string[] }[] } };

  const puzzle = data.puzzle;

  const MAX_SELECTED = 4;
  let selectedMembers: string[] = [];

  const toggleMember = (member: string) => {
    const isSelected = selectedMembers.includes(member);

    if (isSelected) {
      selectedMembers = selectedMembers.filter((m) => m !== member);
    } else {
      if (selectedMembers.length >= MAX_SELECTED) return;
      selectedMembers = [...selectedMembers, member];
    }
  };
  function handleClick(event: MouseEvent): void {
    console.log('Button clicked!', event.currentTarget);
    alert('Hello Svelte with TypeScript!');
  }
</script>

<div class="page">
  {#if puzzle}
    <header class="header">
      <h1 class="title">{puzzle.title}</h1>
    </header>

    <main class="members-grid">
      {#each puzzle.answers as answer}
        {#each answer.members as member}
          <button
            type="button"
            class={`member-card level-${answer.level} ${
              selectedMembers.includes(member) ? 'selected' : ''
            }`}
            on:click={() => toggleMember(member)}
          >
            <span class="member-text">{member}</span>
          </button>
        {/each}
      {/each}
    </main>
      <button on:click={handleClick}>
        Submit
      </button>
  {:else}
    <p class="empty">No puzzle loaded.</p>
  {/if}
</div>

<style>
  .page {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    width: 100vw;
    background-image: url('../lib/assets/background-img.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }

  .members-grid {
    flex: 1;
    display: grid;
    grid-template-columns: repeat(4, minmax(120px, 1fr));
    gap: 0.5rem .5rem;
    max-width: 100rem;
    margin: 0 auto;
    align-content: stretch;
    justify-items: center;
    padding: 2rem 1rem;
    padding-bottom: 15rem;
    
  }

  .header {
    text-align: center;
    padding: 1rem 0;
  }

  .member-card {
    display: flex;
    align-items: center;
    justify-content: center;
    background: #fff;
    border-radius: 12px;
    padding: 1.25rem 1.25rem;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);
    min-width: 140px;
    text-align: center;
    font-size: larger;
    font-family: 'Rethink Sans', sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
    cursor: pointer;
    transition: transform 0.1s ease, box-shadow 0.1s ease, border-color 0.1s ease;
    border: none;
  }

  .member-card:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.16);
  }

  .member-card.selected {
    border: 2px solid #2563eb;
    box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2);
  }

  .member-text {
    font-weight: 500;
  }
</style>
