import {Component, Input, OnInit} from '@angular/core';
import {Categories} from "../Categories";

@Component({
  selector: 'app-category-item',
  templateUrl: './category-item.component.html',
  styleUrls: ['./category-item.component.css']
})
export class CategoryItemComponent implements OnInit {
@Input() category: Categories;
  constructor() { }

  ngOnInit(): void {
  }

}
