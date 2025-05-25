let deleteChannelId = null;

window.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll(".delete-trashbox");
    const deleteModal = document.getElementById("deleteModal");
    const confirmDeleteBtn = document.getElementById("confirmDeleteBtn");
    const cancelDeleteBtn = document.getElementById("cancelDeleteBtn");

    let targetToDelete = null;

    deleteButtons.forEach((btn) => {
        btn.addEventListener("click", (event) => {
            targetToDelete = event.target.closest(".channel-title-box");
            deleteChannelId = targetToDelete.getAttribute("data-channel-id");
            deleteModal.style.display = "flex";
        })
    })

    confirmDeleteBtn.addEventListener("click", () => {
        console.log("削除されるチャンネルID:", deleteChannelId);
        console.log("削除処理通りました");
        deleteModal.style.display = "none";
        targetToDelete = "null";
    })

    cancelDeleteBtn.addEventListener("click", () => {
        deleteModal.style.display = "none";
        targetToDelete = "null";
    })
});