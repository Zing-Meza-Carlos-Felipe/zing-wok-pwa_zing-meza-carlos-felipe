// csr.js — Renderizado en el Cliente (CSR) con Filtros

const contenedorCatalogo = document.getElementById("catalogo");
let productosGlobales = []; // Guardará el catálogo completo para poder filtrar

// 1) fetch() le pide el archivo catalogo.json al servidor
fetch("catalogo.json")
  .then((respuesta) => respuesta.json())
  .then((productos) => {
    productosGlobales = productos; // Guardamos la lista original
    
    // Quitamos los atributos de carga
    contenedorCatalogo.removeAttribute("aria-busy");
    contenedorCatalogo.removeAttribute("aria-label");

    // Mostramos todos los productos la primera vez
    renderizarProductos(productosGlobales);

    // Activamos la lógica de clics para las pestañas de filtro
    configurarFiltros();
  })
  .catch((error) => {
    contenedorCatalogo.innerHTML = "<p>No se pudo cargar el catálogo. Intenta más tarde.</p>";
    contenedorCatalogo.removeAttribute("aria-busy");
    contenedorCatalogo.removeAttribute("aria-label");
    console.error("Error al cargar catálogo:", error);
  });

// 2) Función que dibuja en pantalla el array de productos que se le pase
function renderizarProductos(listaProductos) {
  contenedorCatalogo.innerHTML = ""; // Borramos las tarjetas anteriores

  if (listaProductos.length === 0) {
    contenedorCatalogo.innerHTML = "<p>No hay productos disponibles en esta categoría.</p>";
    return;
  }

  listaProductos.forEach((producto) => {
    const tarjeta = document.createElement("div");
    tarjeta.className = "producto";

    tarjeta.innerHTML = `
      <img class="producto__foto" src="${producto.imagen}" alt="${producto.nombre}" loading="lazy">
      <strong>${producto.nombre}</strong>
      <span class="precio">$${producto.precio}</span>
      <p>Stock: ${producto.stock}</p>
      <button type="button" data-id="${producto.id}">Agregar al carrito</button>
    `;

    contenedorCatalogo.appendChild(tarjeta);

    // Conectamos el botón con agregarAlCarrito() de carrito.js
    tarjeta.querySelector("button").addEventListener("click", () => {
      if (typeof agregarAlCarrito === "function") {
        agregarAlCarrito(producto);
      }
    });
  });
}

// 3) Función para controlar el comportamiento visual y la acción de los botones de filtro
function configurarFiltros() {
  const contenedorFiltros = document.querySelector(".filtros");
  if (!contenedorFiltros) return;

  contenedorFiltros.addEventListener("click", (e) => {
    const boton = e.target.closest(".filtro");
    if (!boton) return;

    // Cambiar la clase activa visualmente
    document.querySelectorAll(".filtro").forEach((btn) => btn.classList.remove("filtro--activo"));
    boton.classList.add("filtro--activo");

    // Filtrar los productos por la categoría seleccionada
    const categoria = boton.dataset.categoria;

    if (categoria === "Todos") {
      renderizarProductos(productosGlobales);
    } else {
      const filtrados = productosGlobales.filter((p) => p.categoria === categoria);
      renderizarProductos(filtrados);
    }
  });
}