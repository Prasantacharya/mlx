/* 
*  Copyright 2021 IBM Corporation
* 
*  Licensed under the Apache License, Version 2.0 (the "License"); 
*  you may not use this file except in compliance with the License. 
*  You may obtain a copy of the License at 
* 
*      http://www.apache.org/licenses/LICENSE-2.0 
* 
*  Unless required by applicable law or agreed to in writing, software 
*  distributed under the License is distributed on an "AS IS" BASIS, 
*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
*  See the License for the specific language governing permissions and 
*  limitations under the License. 
*/ 
import React, { useContext } from 'react'
import StoreContext from '../../lib/stores/context'
import CodaitLogo from '../../icons/codaitLogo';
import { Link } from 'react-router-dom';

interface SideBarHeaderProps {
  name: string;
  active: boolean;
}

const sideNavColors = {
  bg: '#424242',
  fgActive: '#fff',
  fgActiveInvisible: 'rgb(227, 233, 237, 0)',
  fgDefault: '#666',
  hover: '#3f3f3f',
  separator: '#666',
};

const SideBarHeader: React.FunctionComponent<SideBarHeaderProps> = (props) => {
  const { active: isActive } = props

  const { store } = useContext(StoreContext)
  const { value, default: defaultValue } = store.settings.branding.name

  const shortenBrand = (brand: string) => {
    if (brand.length <= 10)
      return brand;

    const split = brand.split(' ')
    let brandAbrev = ""
    split.forEach((word: string) => {
      if (word.toLowerCase() === "exchange")
        brandAbrev += "X"
      else
       brandAbrev += word[0].toUpperCase()
    })
    return brandAbrev
  }

  
  return (
    <div className="sidebar-header-wrap">
      <Link to="/">
        <CodaitLogo 
          color={sideNavColors.fgActive} 
          style={{
            verticalAlign: "middle",
            flexShrink: 0}} 
        />
        <h2 
          className={`sidebar-list-item header ${isActive ? 'active' : 'not-active'}`}>
          {shortenBrand(value || defaultValue)}
        </h2>
      </Link>
      <hr className="sidebar-divider"/>
    </div>
  );
};

export default SideBarHeader;
