function scrollToChapter(chapterId) {
  const chapterElement = document.getElementById(chapterId);
  const scrollableContent = document.getElementById("scrollableContent");
  if (chapterElement && scrollableContent) {
    const scrollOffset = chapterElement.offsetTop - scrollableContent.offsetTop;
    scrollableContent.scrollTop = scrollOffset;
  }
}
