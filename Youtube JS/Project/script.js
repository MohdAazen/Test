let movies=[
    {
        name:"Avengers Endgame",
        poster:"https://lumiere-a.akamaihd.net/v1/images/p_avengersendgame_19751_e14a0104.jpeg",
        rating:8.7

    },
    {
        name:"Oppenheimer",
        poster:"https://res.cloudinary.com/westfielddg/image/upload/przwazayebybnziwleet",
        rating:8.0

    },
    {
        name:"Hera Pheri",
        poster:"https://m.media-amazon.com/images/M/MV5BNDExMTBlZTYtZWMzYi00NmEwLWEzZGYtOTA1MDhmNTc0ODZkXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg",
        rating:9.0

    },
    {
        name:"John Wick 2",
        poster:"https://m.media-amazon.com/images/I/81yqeOUaKPL.jpg",
        rating:7.9

    },
    {
        name:"Kuch Kuch Hota Hai",
        poster:"https://m.media-amazon.com/images/M/MV5BNGNhNWMwNTgtZmNlOS00OGM3LWIxYzItOWQwZDJjMzQ3MzRlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg",
        rating:6.5

    },
    {
        name:"3 idiots",
        poster:"https://www.tallengestore.com/cdn/shop/products/3_Idiots_169ae206-40b7-4c28-83cd-964538827d0c.jpg?v=1582192809",
        rating:9.2

    },
    {
        name:"Border",
        poster:"https://i.etsystatic.com/20387760/r/il/f37074/3272972500/il_fullxfull.3272972500_823s.jpg",
        rating:6.7

    },
    {
        name:"Raaz",
        poster:"https://m.media-amazon.com/images/M/MV5BM2JkYTJjODAtZjYwZS00NTU0LTg1YjAtYzY4YTYxN2VkMTk3XkEyXkFqcGdeQXVyMzc0NzU5MTc@._V1_.jpg",
        rating:9.0

    },
    {
        name:"Rowdy Rathore",
        poster:"https://m.media-amazon.com/images/I/51cjZXaXbmL.jpg",
        rating:6.8

    },
    {
        name:"Dhadkan",
        poster:"https://m.media-amazon.com/images/M/MV5BMDMzZWE4NDUtOWRlMS00ODJjLThmZjAtNWU1MmFiOWVmZmJjXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_.jpg",
        rating:9.1

    },
    {
        name:"Lagaan",
        poster:"https://upload.wikimedia.org/wikipedia/en/b/b6/Lagaan.jpg",
        rating:8.9

    },
    {
        name:"Hum Aapke Hai Kaun",
        poster:"https://m.media-amazon.com/images/M/MV5BZjc0ODAwMmItMmQwMy00MmRmLThjOGYtZGEwYjQ2ZjcyYzA3XkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg",
        rating:7.5

    },
    {
        name:"Mohabbatein",
        poster:"https://m.media-amazon.com/images/M/MV5BYzU5ZGJiYzQtYjA2Yi00MmNmLTlmZmYtZTcxZjBhZGM1NDcxXkEyXkFqcGdeQXVyNTkzNDQ4ODc@._V1_FMjpg_UX1000_.jpg",
        rating:9.0
    },
    {
        name:"Vivah",
        poster:"https://m.media-amazon.com/images/M/MV5BZjNjZWViNTYtYzAzZC00OTY2LWIzMTMtNTcxNzQzNzNiYjc4XkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg",
        rating:8.7

    }
];

function searchMovie()
{
    let movieName = document.getElementById("search").value;
    if(movieName!=="")
    {
        let result = movies.filter(function(movie)
        {
            return movie.name.toUpperCase().includes(movieName.toUpperCase())
        })
        displayMovies(result);
    }
    else{
        displayMovies(movies);
    }
}

    
function displayMovies(data)
    {
        let htmlString = ``;

    for(let i =0;i<data.length;i++)
        {
            document.getElementById("movies").innerHTML="";
            htmlString= htmlString+ `
            <div class="movie">
                <div class="overlay">
                    <div class="video">
                    </div>
                    <div class="details">
                        <h1>${data[i].name}</h1>
                        <h3>IMDB : ${data[i].rating}</h3>
                        <p onclick="doSomething()"> ... </p>
                    </div>
                </div>
            
            <img class="poster" src="${data[i].poster}" alt="poster">
        </div>
            `
        }
    document.getElementById("movies").innerHTML=htmlString;
    }

    displayMovies(movies);

// let movie = document.createElement("div");
    // movie.classList.add("movie");

    // let overlay = document.createElement("div");
    // overlay.classList.add("overlay");

    // movie.appendChild(overlay);

    // console.log(movie,overlay);