// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 20,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});

function fetchAndUpdateGraph() {
    fetch('/home/petarelectro/Vailut/backupStorage/backupGraph.html')
      .then(response => response.text())
      .then(html => {
        document.querySelector('.graph-container').innerHTML = html;
      })
      .catch(error => console.error('Error fetching updated graph:', error));
  }
  
  // Set an interval to update the graph periodically, e.g., every 5 minutes
  setInterval(fetchAndUpdateGraph, 300000); // 300000 milliseconds = 5 minutes
  
  // Optionally, fetch and update the graph immediately on page load
  document.addEventListener('DOMContentLoaded', fetchAndUpdateGraph);

