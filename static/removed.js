const restore_button = document.querySelectorAll(".restore-button")
const job_box = document.querySelectorAll(".jobs-display")
const no_jobs = document.getElementById("no-jobs")
const perm_delete = document.querySelectorAll(".delete-perm-button")

restore_button.forEach((button,index) => {
    button.addEventListener("click", () => changeJob(index, 0))
})
if (job_box.length > 0){
    no_jobs.classList.add("active")
}

perm_delete.forEach((button, index) => {
    button.addEventListener("click", () => deleteJob(index))
})

async function deleteJob(index) {
    const response = await fetch("/deleteJob",{
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            jobId: job_box[index].dataset.id,
        })
    })
    const data = await response.json();
    if (data.status === 200){
        location.reload();
    }
}