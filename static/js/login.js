window.onload = () => {
    const login_form = document.querySelector("#loginform")

    login_form.addEventListener("submit", e => {
        e.preventDefault()

        console.log(document.querySelector("#loginname").value)
        console.log(document.querySelector("#loginpass").value)

        const details = [
            document.querySelector("#loginname").value,
            document.querySelector("#loginpass").value
        ]

        fetch("/logincheck", {
            method: "POST",
            body: JSON.stringify({details}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(rep => rep.json()).then(data => {
            console.log(data)

            if (data["status"] === true) {
                console.log("Correct login :)")
            }
            else {
                console.log("Wrong login >:(")
            }
        })
    })
}