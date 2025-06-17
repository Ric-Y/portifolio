    const inputNome = document.getElementById("inpNome");
    const inputEmail = document.getElementById("inpEmail");
    const btnSalvar = document.getElementById("btnSalvar");
    const listaDados = document.getElementById("listaDados");

    btnSalvar.addEventListener('click', () => {
      const nome = inputNome.value.trim();
      const email = inputEmail.value.trim();

      if (nome && email) {
        const item = document.createElement("li");
        item.innerHTML = `<strong>Nome:</strong> ${nome} | <strong>Email:</strong> ${email}`;
        listaDados.appendChild(item);
      }

      inputNome.value = "";
      inputEmail.value = "";
    });