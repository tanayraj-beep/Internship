document.addEventListener('DOMContentLoaded', ()=>{
	const printBtn = document.getElementById('printBtn')
	if(printBtn){
		printBtn.addEventListener('click', ()=>{
			window.print()
		})
	}
})

// Kept simple and dependency-free to satisfy the "three files only" requirement.

