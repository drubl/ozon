import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-nav-category',
  templateUrl: './nav-category.component.html',
  styleUrls: ['./nav-category.component.scss']
})
export class NavCategoryComponent implements OnInit {
    toggleModalCategory = false;

  constructor() { }

  ngOnInit() {
  }

  eventMouseEnterModalCategory() {
    this.toggleModalCategory = true;
  }

  eventMouseLeaveModalCategory(event) {
    if (!(event.toElement.className.includes('modal-login'))) {
      this.toggleModalCategory = false;
    }
  }
}
