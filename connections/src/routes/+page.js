
export async function load({ fetch }) {
 
  const date = '2023-06-12';

  const res = await fetch(`http://127.0.0.1:8000/data/${date}`);
  if (!res.ok) {
    
    return { puzzle: null };
  }

  const puzzle = await res.json();

  
  return { puzzle };
}
