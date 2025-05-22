window.addEventListener("DOMContentLoaded", () => {
    const logoutModalOpen = document.getElementById("logoutModalOpen");
    const logoutModal = document.getElementById("logoutModal");
    const confirmLogoutBtn = document.getElementById("confirmLogoutBtn");
    const cancelLogoutBtn = document.getElementById("cancelLogoutBtn");

    logoutModalOpen.addEventListener("click", () => {
        logoutModal.style.display = "flex";
    })

    confirmLogoutBtn.addEventListener("click", () => {
        // fetch("/logout", {
            //   method: "POST",
            //   headers: {
            //     "Content-Type": "application/json"
            //   },
            //   body: JSON.stringify({})
            // })
            // .then(response => {
            //   if (response.ok) {
            //     window.location.href = "/login";
            //   } else {
            //     console.error("ログアウト失敗");
            //   }
            // })
            // .catch(error => {
            //   console.error("通信エラー:", error);
            // });
        window.location.href = "/login";
        logoutModal.style.display = "none";
    })

    cancelLogoutBtn.addEventListener("click", () => {
        logoutModal.style.display = "none";
    })
});