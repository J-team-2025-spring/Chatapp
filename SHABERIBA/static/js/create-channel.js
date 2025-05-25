let isEditMode = false;
let editChannelId = null;

window.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("channelModal");
  const modalTitle = document.getElementById("modalTitle");
  const openCreateBtn = document.getElementById("openModalBtn");
  const closeBtn = document.getElementById("closeModalBtn");
  const inputName = document.getElementById("channelName");
  const inputSummary = document.getElementById("channelSummary");
  const form = document.getElementById("channelForm");

  openCreateBtn.addEventListener("click", () => {
    console.log("モーダル起動")
    isEditMode = false;
    editChannelId = null;
    form.action = "/channels";
    form.method = "POST";
    form.submit();

    modalTitle.textContent = "チャンネル作成";
    inputName.value = "";
    inputSummary.value = "";    
    modal.style.display = "flex";
  });

  const editButtons = document.querySelectorAll(".edit-pen");

  editButtons.forEach((btn) => {
    btn.addEventListener("click", (event) => {
      isEditMode = true;

      modalTitle.textContent = "チャンネル編集";

      const channelBox = event.target.closest(".channel-title-box");
      editChannelId = channelBox.getAttribute("data-channel-id");

      form.action = `/channels/edit/${editChannelId}`;
      form.method = "POST";
      form.submit();
      
      const title = channelBox.querySelector(".channel-title").textContent.trim();
      const summary = channelBox.querySelector(".channel-summary").textContent.trim();

      inputName.value = title;
      inputSummary.value = summary;
      
      modal.style.display = "flex";
    })
  })

  // form.addEventListener("submit", (event) => {
  //   event.preventDefault();

  //   const name = inputName.value;
  //   const summary = inputSummary.value;


  //   // if (isEditMode) {
  //   //   console.log("編集モード")
  //   //   console.log("チャンネルID：", editChannelId);
  //   //   console.log("編集したチャンネル名：", name);
  //   //   console.log("編集したチャンネル概要：", summary);
  //   // } else{
  //   //   console.log("作成モード")
  //   //   console.log("チャンネル名：", name);
  //   //   console.log("チャンネル概要：", summary);
  //   // }

  // })

  closeBtn.addEventListener("click", () => {
    modal.style.display = "none";
  });
});