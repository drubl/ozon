import {Component, Input, OnInit} from '@angular/core';
import {Categories} from "../../../../Categories";

@Component({
  selector: 'app-category-side-bar',
  templateUrl: './category-side-bar.component.html',
  styleUrls: ['./category-side-bar.component.css']
})
export class CategorySideBarComponent implements OnInit {
@Input() category: Categories;
  constructor() { }

  ngOnInit(): void {
  }
}
