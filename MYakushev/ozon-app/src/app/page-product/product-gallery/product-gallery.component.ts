import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-product-gallery',
  templateUrl: './product-gallery.component.html',
  styleUrls: ['./product-gallery.component.css']
})
export class ProductGalleryComponent implements OnInit {
  @Input() productImg;
  constructor() { }

  ngOnInit(): void {
  }

}
