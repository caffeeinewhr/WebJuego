document.querySelectorAll('.carta').forEach((card) => {
    let boundingRect = null;
  
    card.addEventListener('mouseenter', (ev) => {
      boundingRect = ev.currentTarget.getBoundingClientRect();
    });
  
    card.addEventListener('mouseleave', () => {
      boundingRect = null;
      card.style.transform = '';
    });
  
    card.addEventListener('mousemove', (ev) => {
      if (!boundingRect) return;
      const x = ev.clientX - boundingRect.left;
      const y = ev.clientY - boundingRect.top;
      const xPercentage = x / boundingRect.width;
      const yPercentage = y / boundingRect.height;
      const xRotation = (xPercentage - 0.5) * 20;
      const yRotation = (0.5 - yPercentage) * 20;
  
      card.style.transform = `rotateX(${yRotation}deg) rotateY(${xRotation}deg) scale(1.1)`;
    });
  });
  