* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: #e9e9e9;
}

/* ============================
   ESCRITORIO (width > 780px)
   min-width: 380px / max-width: 1500px
   ============================ */
.pagina {
    min-width: 380px;
    max-width: 1500px;
    margin: 0 auto;
    min-height: 100vh;
    background-color: #bdd7ee;
    display: grid;
    grid-template-columns: 250px 1fr;
    grid-template-rows: 80px 1fr 60px;
    grid-template-areas:
        "header header"
        "aside  main"
        "footer footer";
    border: 1px solid #1f3a56;
}

header {
    grid-area: header;
    background-color: #5b9bd5;
    display: flex;
    align-items: center;
    padding: 0 30px;
    border-bottom: 1px solid #1f3a56;
}

.boton {
    background-color: #c55a11;
    color: #fff;
    text-decoration: none;
    padding: 10px 28px;
    border: 1px solid #1f3a56;
    border-radius: 6px;
}

aside {
    grid-area: aside;
    background-color: #deeaf6;
    border-right: 1px solid #1f3a56;
    padding: 20px;
}

main {
    grid-area: main;
    padding: 15px;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

footer {
    grid-area: footer;
    background-color: #5b9bd5;
    border-top: 1px solid #1f3a56;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Banner */
.banner {
    background-color: #fce4d6;
    border: 1px solid #1f3a56;
    height: 90px;
    padding: 10px;
}

/* 4 cuadrados en una fila */
.cuadrados {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
}

.cuadrado {
    background-color: #b4c7e7;
    border: 1px solid #1f3a56;
    aspect-ratio: 1 / 1;
    padding: 10px;
}

/* Verde alto a la izquierda + 2 grises apilados a la derecha */
.contenido {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    grid-template-rows: 1fr 1fr;
    gap: 15px;
    min-height: 260px;
}

.verde {
    grid-row: 1 / 3;
    background-color: #548235;
    border: 1px solid #1f3a56;
    padding: 10px;
    color: #fff;
}

.gris {
    background-color: #c9c9c9;
    border: 1px solid #1f3a56;
    padding: 10px;
}

/* ============================
   TABLET (width <= 780px)
   El menú lateral pasa a ser una barra bajo el header
   ============================ */
@media screen and (max-width: 780px) {
    .pagina {
        grid-template-columns: 1fr;
        grid-template-rows: 80px 80px 1fr 60px;
        grid-template-areas:
            "header"
            "aside"
            "main"
            "footer";
    }

    aside {
        border-right: none;
        border-bottom: 1px solid #1f3a56;
    }
}

/* ============================
   MÓVIL (width <= 480px)
   ============================ */
@media screen and (max-width: 480px) {
    /* Botón centrado */
    header {
        justify-content: center;
    }

    /* Cuadrados en 2 x 2 (más anchos que altos) */
    .cuadrados {
        grid-template-columns: repeat(2, 1fr);
    }

    .cuadrado {
        aspect-ratio: auto;
        height: 60px;
    }

    /* Verde a todo el ancho, grises uno al lado del otro */
    .contenido {
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto auto;
        min-height: 0;
    }

    .verde {
        grid-column: 1 / 3;
        grid-row: auto;
        height: 60px;
    }

    .gris {
        height: 65px;
    }
}