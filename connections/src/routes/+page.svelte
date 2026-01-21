<script>
  import '../app.css'
  export let data;
  const puzzle = data.puzzle;
</script>
<div class="page">
{#if puzzle}
  
    <header class="header">
      <h1 class="title">{puzzle.title}</h1>
    </header>

    <main class="members-grid">
  {#each puzzle.answers as answer}
    {#each answer.members as member}
      <section class={`member-card level-${answer.level}`}>
        <span class="member-text">{member}</span>
      </section>
    {/each}
  {/each}
</main>


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
    background-image:url('../lib/assets/background-img.jpg'); 
    background-size: cover;            
    background-position: center;       
    background-repeat: no-repeat;
    
  }

  .members-grid {
    flex: 1;                  
    display: grid;
    grid-template-columns: repeat(4, minmax(120px, 1fr));
    gap: .5rem 2rem;
    max-width: 700px;
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
    box-shadow: 0 2px 6px rgba(0,0,0,0.12);
    min-width: 140px;
    text-align: center;
    font-size: larger;
    font-family: "Rethink Sans", sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
  }

  

  .member-text {
    font-weight: 500;
  }
</style>
