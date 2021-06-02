<script>
    
    function Excluir_cliente(pk) {
        Swal.fire({
        "title" : "Tem certeza que deseja excluir?",
        "text" : "Essa ação não poderar ser desfeita!!",
        "icon" : "question",
        "showCancelButton" : true,
        "cancelButtonText" : "Não, cancelar",
        "confirmButtonText" : "Sim",
        "confirmButtonColor" : "#dc3545"
        })

        .then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/deletar/cliente/" + pk 
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            Swal.fire({
            "title" : "Cancelado",
            "text" : "Ação cancelada com sucesso!!",
            "icon" : "error"
            })
        }
        })
    }

    function Excluir_despesa(pk) {
        Swal.fire({
        "title" : "Tem certeza que deseja excluir?",
        "text" : "Essa ação não poderar ser desfeita!!",
        "icon" : "question",
        "showCancelButton" : true,
        "cancelButtonText" : "Não, cancelar",
        "confirmButtonText" : "Sim",
        "confirmButtonColor" : "#dc3545"
        })

        .then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/deletar/despesa/" + pk 
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            Swal.fire({
            "title" : "Cancelado",
            "text" : "Ação cancelada com sucesso!!",
            "icon" : "error"
            })
        }
        })
    }

    function Excluir_endereco(pk) {
        Swal.fire({
            "title" : "Tem certeza que deseja excluir?",
            "text" : "Essa ação não poderar ser desfeita!!",
            "icon" : "question",
            "showCancelButton" : true,
            "cancelButtonText" : "Não, cancelar",
            "confirmButtonText" : "Sim",
            "confirmButtonColor" : "#dc3545"
            })

            .then((result) => {
            if (result.isConfirmed) {
                window.location.href = "/deletar/endereco/" + pk 
            } else if (
                /* Read more about handling dismissals below */
                result.dismiss === Swal.DismissReason.cancel
            ) {
                Swal.fire({
                "title" : "Cancelado",
                "text" : "Ação cancelada com sucesso!!",
                "icon" : "error"
                })
            }
            })
        }      

    function Excluir_fornecedor(pk) {
        Swal.fire({
        "title" : "Tem certeza que deseja excluir?",
        "text" : "Essa ação não poderar ser desfeita!!",
        "icon" : "question",
        "showCancelButton" : true,
        "cancelButtonText" : "Não, cancelar",
        "confirmButtonText" : "Sim",
        "confirmButtonColor" : "#dc3545"
        })

        .then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/deletar/fornecedor/" + pk 
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            Swal.fire({
            "title" : "Cancelado",
            "text" : "Ação cancelada com sucesso!!",
            "icon" : "error"
            })
        }
        })
    }

    function Excluir_funcionario(pk) {
        Swal.fire({
        "title" : "Tem certeza que deseja excluir?",
        "text" : "Essa ação não poderar ser desfeita!!",
        "icon" : "question",
        "showCancelButton" : true,
        "cancelButtonText" : "Não, cancelar",
        "confirmButtonText" : "Sim",
        "confirmButtonColor" : "#dc3545"
        })

        .then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/deletar/funcionario/" + pk 
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            Swal.fire({
            "title" : "Cancelado",
            "text" : "Ação cancelada com sucesso!!",
            "icon" : "error"
            })
        }
        })
    }

    function Excluir_funcao(pk) {
        Swal.fire({
        "title" : "Tem certeza que deseja excluir?",
        "text" : "Essa ação não poderar ser desfeita!!",
        "icon" : "question",
        "showCancelButton" : true,
        "cancelButtonText" : "Não, cancelar",
        "confirmButtonText" : "Sim",
        "confirmButtonColor" : "#dc3545"
        })

        .then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/deletar/funcao/" + pk 
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            Swal.fire({
            "title" : "Cancelado",
            "text" : "Ação cancelada com sucesso!!",
            "icon" : "error"
            })
        }
        })
    }

    function Excluir_produto(pk) {
        Swal.fire({
        "title" : "Tem certeza que deseja excluir?",
        "text" : "Essa ação não poderar ser desfeita!!",
        "icon" : "question",
        "showCancelButton" : true,
        "cancelButtonText" : "Não, cancelar",
        "confirmButtonText" : "Sim",
        "confirmButtonColor" : "#dc3545"
        })

        .then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/deletar/produto/" + pk 
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            Swal.fire({
            "title" : "Cancelado",
            "text" : "Ação cancelada com sucesso!!",
            "icon" : "error"
            })
        }
        })
    }

    function Excluir_venda(pk) {
        Swal.fire({
        "title" : "Tem certeza que deseja excluir?",
        "text" : "Essa ação não poderar ser desfeita!!",
        "icon" : "question",
        "showCancelButton" : true,
        "cancelButtonText" : "Não, cancelar",
        "confirmButtonText" : "Sim",
        "confirmButtonColor" : "#dc3545"
        })

        .then((result) => {
        if (result.isConfirmed) {
            window.location.href = "/deletar/venda/" + pk 
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            Swal.fire({
            "title" : "Cancelado",
            "text" : "Ação cancelada com sucesso!!",
            "icon" : "error"
            })
        }
        })
    }

</script>