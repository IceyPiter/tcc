function toggleRule(ruleNumber) {
    var content = document.getElementById("rule-content-" + ruleNumber);
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
    } else {
        content.style.display = "none";
    }
}

const years = document.querySelectorAll(".year");

  years.forEach(year => {
      year.addEventListener("click", () => {
          years.forEach(otherYear => {
              if (otherYear !== year) {
                  otherYear.classList.remove("active");
                  otherYear.querySelector(".event-info").style.display = "none";
              }
          });

          if (!year.classList.contains("active")) {
              year.classList.add("active");
              year.querySelector(".event-info").style.display = "block";
          } else {
              year.classList.remove("active");
              year.querySelector(".event-info").style.display = "none";
          }
      });
  });


document.getElementById("textosMensage").addEventListener("click", function (event) {
    // Pega o ID do elemento que foi clicado
    var elementoClicadoUser = event.target.name;
    var elementoClicadoID = event.target.id

    // Verifique se o elemento clicado tem um ID (evita erros se não tiver)
    if (elementoClicadoUser) {       
        // Exibe o ID e o conteúdo em outro espaço (por exemplo, em um div)
        document.getElementById("responde").innerHTML = "Respondendo: "
        document.getElementById("nome").innerHTML = "" + elementoClicadoUser
        document.getElementById("idresponse").value = "" + elementoClicadoID
    }
});

function toggleForm(formId) {
    // Esconder todos os formulários
    document.getElementById('form1').style.display = 'none';
    document.getElementById('form2').style.display = 'none';
    document.getElementById('form3').style.display = 'none';

    // Mostrar o formulário específico
    document.getElementById(formId).style.display = 'block';
}

function esconderBotao(formId) {
    // Mostrar o formulário específico
    document.getElementById(formId).style.display = 'none';
}
