<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Data Penjualan</h1>

  <h2>Jumlah Penjualan per Item:</h2>
  <ul>
    <% dataAdmin.cartData.products.forEach(item=> { %>
      <li>Produk ID: <%= item.product_id %>, Jumlah Terjual: <%= item.stock_quantity %>
      </li>
      <% }); %>
  </ul>

  
  <h2>Penjualan Terbaru:</h2>
  <ul>
    <% dataAdmin.cartData.latestSales.forEach(sale=> { %>
      <li>Produk ID: <%= sale.product_id %>, Jumlah: <%= sale.quantity %>
      </li>
    <% }); %>
  </ul>

  <canvas id="myChart"></canvas>
</body>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    const dates = tes.map(entry => entry.date);
    const totalProduk1 = tes.map(entry => entry._sum.total);
    const totalProduk2 = tes1.map(entry => entry._sum.total);

    // Create a chart
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: dates,
        datasets: [
          {
            label: 'Produk 1',
            data: totalProduk1,
            backgroundColor: 'rgba(255, 99, 132, 0.5)', // Adjust color as needed
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
          },
          {
            label: 'Produk 2',
            data: totalProduk2,
            backgroundColor: 'rgba(75, 192, 192, 0.5)', // Adjust color as needed
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }
        ]
      },
      options: {
        scales: {
          x: { stacked: true }, // Stack bars on the x-axis
          y: { stacked: true }  // Stack bars on the y-axis
        }
      }
    });
  </script>
</html>