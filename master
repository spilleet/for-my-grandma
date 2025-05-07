import React, { useState } from 'react';
import { MapPin, Calendar, Users, CheckCircle, ArrowLeft, PlusCircle, Search, Clock } from 'lucide-react';

const BasketballApp = () => {
  const [currentScreen, setCurrentScreen] = useState('map');
  const [selectedRegion, setSelectedRegion] = useState(null);
  const [selectedCity, setSelectedCity] = useState(null);

  const handleRegionSelect = (region) => {
    setSelectedRegion(region);
    setCurrentScreen('regionDetail');
  };

  const handleCitySelect = (city) => {
    setSelectedCity(city);
    setCurrentScreen('matchOptions');
  };

  const handleBack = () => {
    if (currentScreen === 'regionDetail') {
      setCurrentScreen('map');
      setSelectedRegion(null);
    } else if (currentScreen === 'matchOptions') {
      setCurrentScreen('regionDetail');
      setSelectedCity(null);
    } else if (['createMatch', 'joinMatch', 'confirmation'].includes(currentScreen)) {
      setCurrentScreen('matchOptions');
    }
  };

  // 메인 지도 화면
  const MapScreen = () => (
    <div className="flex flex-col h-full">
      <div className="bg-blue-600 text-white p-4 text-center shadow-md">
        <h1 className="text-xl font-bold">장애인 농구 매치</h1>
      </div>
      
      <div className="p-4 flex-1 bg-blue-50">
        <h2 className="text-lg font-semibold text-blue-800 mb-4">지역을 선택하세요</h2>
        
        <div className="relative w-full h-64 bg-white rounded-lg shadow-md overflow-hidden mb-4">
          {/* 한국 지도 시각화 (간략화) */}
          <div className="absolute w-full h-full p-2">
            <svg viewBox="0 0 400 600" className="w-full h-full">
              {/* 서울 - 왼쪽 상단으로 이동 */}
              <circle cx="100" cy="120" r="40" fill="#1e88e5" className="cursor-pointer" 
                      onClick={() => handleRegionSelect('서울')} />
              <text x="100" y="120" textAnchor="middle" fill="white" fontSize="22" fontWeight="bold">서울</text>
              
              {/* 경상도 - 오른쪽 하단으로 이동 */}
              <circle cx="320" cy="400" r="40" fill="#1e88e5" className="cursor-pointer"
                      onClick={() => handleRegionSelect('경상도')} />
              <text x="320" y="400" textAnchor="middle" fill="white" fontSize="22" fontWeight="bold">경상</text>
              
              {/* 전라도 - 왼쪽 하단으로 이동 */}
              <circle cx="80" cy="400" r="40" fill="#1e88e5" className="cursor-pointer"
                      onClick={() => handleRegionSelect('전라도')} />
              <text x="80" y="400" textAnchor="middle" fill="white" fontSize="22" fontWeight="bold">전라</text>
              
              {/* 충청도 - 중앙으로 이동 */}
              <circle cx="200" cy="250" r="40" fill="#1e88e5" className="cursor-pointer"
                      onClick={() => handleRegionSelect('충청도')} />
              <text x="200" y="250" textAnchor="middle" fill="white" fontSize="22" fontWeight="bold">충청</text>
              
              {/* 강원도 - 오른쪽 상단으로 이동 */}
              <circle cx="300" cy="120" r="40" fill="#1e88e5" className="cursor-pointer"
                      onClick={() => handleRegionSelect('강원도')} />
              <text x="300" y="120" textAnchor="middle" fill="white" fontSize="22" fontWeight="bold">강원</text>
              
              {/* 제주도 - 더 아래로 이동 */}
              <circle cx="200" cy="520" r="35" fill="#1e88e5" className="cursor-pointer"
                      onClick={() => handleRegionSelect('제주도')} />
              <text x="200" y="520" textAnchor="middle" fill="white" fontSize="20" fontWeight="bold">제주</text>
              
              {/* 연결 점선 - 새 위치에 맞게 조정 */}
              <line x1="120" y1="150" x2="180" y2="220" stroke="#90caf9" strokeWidth="3" strokeDasharray="5,5" />
              <line x1="280" y1="150" x2="220" y2="220" stroke="#90caf9" strokeWidth="3" strokeDasharray="5,5" />
              <line x1="180" y1="280" x2="100" y2="360" stroke="#90caf9" strokeWidth="3" strokeDasharray="5,5" />
              <line x1="220" y1="280" x2="290" y2="360" stroke="#90caf9" strokeWidth="3" strokeDasharray="5,5" />
              <line x1="200" y1="290" x2="200" y2="480" stroke="#90caf9" strokeWidth="3" strokeDasharray="5,5" />
            </svg>
          </div>
        </div>
        
        <div className="bg-white rounded-lg shadow-md p-4">
          <div className="flex items-center text-blue-800 mb-2">
            <MapPin size={18} className="mr-2 text-blue-600" />
            <h3 className="font-medium">인기 지역</h3>
          </div>
          <div className="grid grid-cols-2 gap-2">
            <button 
              className="bg-blue-100 text-blue-700 p-2 rounded-md flex items-center justify-center"
              onClick={() => handleRegionSelect('서울')}
            >
              서울
            </button>
            <button 
              className="bg-blue-100 text-blue-700 p-2 rounded-md flex items-center justify-center"
              onClick={() => handleRegionSelect('부산')}
            >
              부산
            </button>
            <button 
              className="bg-blue-100 text-blue-700 p-2 rounded-md flex items-center justify-center"
              onClick={() => handleRegionSelect('대구')}
            >
              대구
            </button>
            <button 
              className="bg-blue-100 text-blue-700 p-2 rounded-md flex items-center justify-center"
              onClick={() => handleRegionSelect('인천')}
            >
              인천
            </button>
          </div>
        </div>
      </div>
      
      <div className="bg-white p-2 shadow-lg border-t border-blue-200 flex justify-around">
        <button className="flex flex-col items-center text-blue-700">
          <MapPin size={24} />
          <span className="text-xs">지역</span>
        </button>
        <button className="flex flex-col items-center text-blue-400">
          <Calendar size={24} />
          <span className="text-xs">일정</span>
        </button>
        <button className="flex flex-col items-center text-blue-400">
          <Users size={24} />
          <span className="text-xs">커뮤니티</span>
        </button>
        <button className="flex flex-col items-center text-blue-400">
          <MapPin size={24} />
          <span className="text-xs">프로필</span>
        </button>
      </div>
    </div>
  );
  
  // 지역 세부 화면
  const RegionDetailScreen = () => (
    <div className="flex flex-col h-full">
      <div className="bg-blue-600 text-white p-4 flex items-center shadow-md">
        <button onClick={handleBack} className="mr-2">
          <ArrowLeft size={24} />
        </button>
        <h1 className="text-xl font-bold">{selectedRegion}</h1>
      </div>
      
      <div className="p-4 flex-1 bg-blue-50">
        <div className="flex items-center bg-white rounded-lg shadow-md p-3 mb-4">
          <Search size={20} className="text-blue-400 mr-2" />
          <input 
            type="text" 
            placeholder="지역 검색" 
            className="flex-1 outline-none text-blue-800" 
          />
        </div>
        
        <h2 className="text-lg font-semibold text-blue-800 mb-3">세부 지역</h2>
        
        <div className="space-y-2">
          {selectedRegion === '서울' && (
            <>
              <button 
                className="w-full bg-white p-3 rounded-lg shadow-sm flex justify-between items-center border-l-4 border-blue-500"
                onClick={() => handleCitySelect('강남구')}
              >
                <span className="text-blue-800 font-medium">강남구</span>
                <span className="text-blue-500 text-sm">12개 경기장</span>
              </button>
              <button 
                className="w-full bg-white p-3 rounded-lg shadow-sm flex justify-between items-center"
                onClick={() => handleCitySelect('송파구')}
              >
                <span className="text-blue-800 font-medium">송파구</span>
                <span className="text-blue-500 text-sm">8개 경기장</span>
              </button>
              <button 
                className="w-full bg-white p-3 rounded-lg shadow-sm flex justify-between items-center"
                onClick={() => handleCitySelect('마포구')}
              >
                <span className="text-blue-800 font-medium">마포구</span>
                <span className="text-blue-500 text-sm">6개 경기장</span>
              </button>
              <button 
                className="w-full bg-white p-3 rounded-lg shadow-sm flex justify-between items-center"
                onClick={() => handleCitySelect('서대문구')}
              >
                <span className="text-blue-800 font-medium">서대문구</span>
                <span className="text-blue-500 text-sm">5개 경기장</span>
              </button>
            </>
          )}
          
          {selectedRegion === '경상도' && (
            <>
              <button 
                className="w-full bg-white p-3 rounded-lg shadow-sm flex justify-between items-center"
                onClick={() => handleCitySelect('부산')}
              >
                <span className="text-blue-800 font-medium">부산</span>
                <span className="text-blue-500 text-sm">15개 경기장</span>
              </button>
              <button 
                className="w-full bg-white p-3 rounded-lg shadow-sm flex justify-between items-center"
                onClick={() => handleCitySelect('대구')}
              >
                <span className="text-blue-800 font-medium">대구</span>
                <span className="text-blue-500 text-sm">9개 경기장</span>
              </button>
              <button 
                className="w-full bg-white p-3 rounded-lg shadow-sm flex justify-between items-center"
                onClick={() => handleCitySelect('울산')}
              >
                <span className="text-blue-800 font-medium">울산</span>
                <span className="text-blue-500 text-sm">7개 경기장</span>
              </button>
            </>
          )}
          
          {/* 다른 지역들에 대한 세부 지역도 필요에 따라 추가 */}
        </div>
      </div>
    </div>
  );
  
  // 매치 옵션 화면
  const MatchOptionsScreen = () => (
    <div className="flex flex-col h-full">
      <div className="bg-blue-600 text-white p-4 flex items-center shadow-md">
        <button onClick={handleBack} className="mr-2">
          <ArrowLeft size={24} />
        </button>
        <h1 className="text-xl font-bold">{selectedRegion} {selectedCity}</h1>
      </div>
      
      <div className="p-4 flex-1 bg-blue-50">
        <div className="grid grid-cols-1 gap-4">
          <button 
            className="bg-blue-600 text-white p-6 rounded-lg shadow-md flex flex-col items-center justify-center h-40"
            onClick={() => setCurrentScreen('createMatch')}
          >
            <PlusCircle size={48} className="mb-2" />
            <span className="text-xl font-bold">경기 등록하기</span>
            <span className="text-sm mt-1">나만의 농구 경기를 만들어보세요</span>
          </button>
          
          <button 
            className="bg-blue-500 text-white p-6 rounded-lg shadow-md flex flex-col items-center justify-center h-40"
            onClick={() => setCurrentScreen('joinMatch')}
          >
            <Users size={48} className="mb-2" />
            <span className="text-xl font-bold">경기 신청하기</span>
            <span className="text-sm mt-1">열린 농구 경기에 참여해보세요</span>
          </button>
        </div>
      </div>
    </div>
  );
  
  // 경기 등록 화면
  const CreateMatchScreen = () => (
    <div className="flex flex-col h-full">
      <div className="bg-blue-600 text-white p-4 flex items-center shadow-md">
        <button onClick={handleBack} className="mr-2">
          <ArrowLeft size={24} />
        </button>
        <h1 className="text-xl font-bold">경기 등록하기</h1>
      </div>
      
      <div className="p-4 flex-1 bg-blue-50 overflow-auto">
        <div className="bg-white rounded-lg shadow-md p-4 mb-4">
          <h2 className="text-blue-800 font-semibold mb-2">경기장 선택</h2>
          <select className="w-full p-2 border border-blue-200 rounded text-blue-800 bg-blue-50">
            <option>장소를 선택하세요</option>
            <option>휠체어 접근성 좋은 농구장 A</option>
            <option>장애인 체육센터 B</option>
            <option>종합운동장 C</option>
          </select>
        </div>
        
        <div className="bg-white rounded-lg shadow-md p-4 mb-4">
          <h2 className="text-blue-800 font-semibold mb-2">날짜 및 시간</h2>
          <input type="date" className="w-full p-2 border border-blue-200 rounded mb-2 text-blue-800 bg-blue-50" />
          <div className="flex space-x-2">
            <select className="flex-1 p-2 border border-blue-200 rounded text-blue-800 bg-blue-50">
              <option>시작 시간</option>
              <option>14:00</option>
              <option>15:00</option>
              <option>16:00</option>
            </select>
            <select className="flex-1 p-2 border border-blue-200 rounded text-blue-800 bg-blue-50">
              <option>종료 시간</option>
              <option>16:00</option>
              <option>17:00</option>
              <option>18:00</option>
            </select>
          </div>
        </div>
        
        <div className="bg-white rounded-lg shadow-md p-4 mb-4">
          <h2 className="text-blue-800 font-semibold mb-2">참가자 정보</h2>
          <div className="flex space-x-2 mb-2">
            <select className="flex-1 p-2 border border-blue-200 rounded text-blue-800 bg-blue-50">
              <option>필요 인원</option>
              <option>4명</option>
              <option>6명</option>
              <option>8명</option>
              <option>10명</option>
            </select>
            <select className="flex-1 p-2 border border-blue-200 rounded text-blue-800 bg-blue-50">
              <option>난이도</option>
              <option>초보자 환영</option>
              <option>중급자</option>
              <option>상급자</option>
            </select>
          </div>
          <input 
            type="text" 
            placeholder="추가 요구사항 (휠체어 접근성 등)" 
            className="w-full p-2 border border-blue-200 rounded text-blue-800 bg-blue-50" 
          />
        </div>
        
        <div className="bg-white rounded-lg shadow-md p-4 mb-4">
          <h2 className="text-blue-800 font-semibold mb-2">경기 설명</h2>
          <textarea 
            placeholder="경기에 대한 설명과 참가자에게 전달할 내용을 작성해주세요" 
            className="w-full p-2 border border-blue-200 rounded h-24 text-blue-800 bg-blue-50"
          ></textarea>
        </div>
        
        <button 
          className="w-full bg-blue-600 text-white p-4 rounded-lg font-bold shadow-md"
          onClick={() => setCurrentScreen('confirmation')}
        >
          경기 등록하기
        </button>
      </div>
    </div>
  );
  
  // 경기 신청 화면
  const JoinMatchScreen = () => (
    <div className="flex flex-col h-full">
      <div className="bg-blue-600 text-white p-4 flex items-center shadow-md">
        <button onClick={handleBack} className="mr-2">
          <ArrowLeft size={24} />
        </button>
        <h1 className="text-xl font-bold">경기 신청하기</h1>
      </div>
      
      <div className="p-4 flex-1 bg-blue-50 overflow-auto">
        <div className="flex items-center bg-white rounded-lg shadow-md p-3 mb-4">
          <Search size={20} className="text-blue-400 mr-2" />
          <input 
            type="text" 
            placeholder="경기 검색" 
            className="flex-1 outline-none text-blue-800" 
          />
        </div>
        
        <div className="space-y-3">
          <div className="bg-white rounded-lg shadow-md p-4 border-l-4 border-blue-500">
            <div className="flex justify-between items-start mb-2">
              <h2 className="font-bold text-blue-800">휠체어 친화적인 농구 모임</h2>
              <span className="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">초보자 환영</span>
            </div>
            
            <div className="space-y-2 mb-3">
              <div className="flex items-center text-blue-700">
                <MapPin size={16} className="mr-1" />
                <span className="text-sm">장애인 체육센터 B</span>
              </div>
              <div className="flex items-center text-blue-700">
                <Calendar size={16} className="mr-1" />
                <span className="text-sm">2025년 4월 20일</span>
              </div>
              <div className="flex items-center text-blue-700">
                <Clock size={16} className="mr-1" />
                <span className="text-sm">14:00 - 16:00</span>
              </div>
              <div className="flex items-center text-blue-700">
                <Users size={16} className="mr-1" />
                <span className="text-sm">4/8명 참가 중</span>
              </div>
            </div>
            
            <button 
              className="w-full bg-blue-600 text-white p-2 rounded font-medium"
              onClick={() => setCurrentScreen('confirmation')}
            >
              참가 신청하기
            </button>
          </div>
          
          <div className="bg-white rounded-lg shadow-md p-4">
            <div className="flex justify-between items-start mb-2">
              <h2 className="font-bold text-blue-800">주말 농구 모임</h2>
              <span className="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">중급자</span>
            </div>
            
            <div className="space-y-2 mb-3">
              <div className="flex items-center text-blue-700">
                <MapPin size={16} className="mr-1" />
                <span className="text-sm">종합운동장 C</span>
              </div>
              <div className="flex items-center text-blue-700">
                <Calendar size={16} className="mr-1" />
                <span className="text-sm">2025년 4월 21일</span>
              </div>
              <div className="flex items-center text-blue-700">
                <Clock size={16} className="mr-1" />
                <span className="text-sm">16:00 - 18:00</span>
              </div>
              <div className="flex items-center text-blue-700">
                <Users size={16} className="mr-1" />
                <span className="text-sm">6/10명 참가 중</span>
              </div>
            </div>
            
            <button 
              className="w-full bg-blue-600 text-white p-2 rounded font-medium"
              onClick={() => setCurrentScreen('confirmation')}
            >
              참가 신청하기
            </button>
          </div>
          
          <div className="bg-white rounded-lg shadow-md p-4">
            <div className="flex justify-between items-start mb-2">
              <h2 className="font-bold text-blue-800">정기 농구 모임</h2>
              <span className="bg-blue-100 text-blue-700 text-xs px-2 py-1 rounded">모든 레벨</span>
            </div>
            
            <div className="space-y-2 mb-3">
              <div className="flex items-center text-blue-700">
                <MapPin size={16} className="mr-1" />
                <span className="text-sm">휠체어 접근성 좋은 농구장 A</span>
              </div>
              <div className="flex items-center text-blue-700">
                <Calendar size={16} className="mr-1" />
                <span className="text-sm">2025년 4월 23일</span>
              </div>
              <div className="flex items-center text-blue-700">
                <Clock size={16} className="mr-1" />
                <span className="text-sm">15:00 - 17:00</span>
              </div>
              <div className="flex items-center text-blue-700">
                <Users size={16} className="mr-1" />
                <span className="text-sm">2/6명 참가 중</span>
              </div>
            </div>
            
            <button 
              className="w-full bg-blue-600 text-white p-2 rounded font-medium"
              onClick={() => setCurrentScreen('confirmation')}
            >
              참가 신청하기
            </button>
          </div>
        </div>
      </div>
    </div>
  );
  
  // 확인 화면
  const ConfirmationScreen = () => (
    <div className="flex flex-col h-full">
      <div className="bg-blue-600 text-white p-4 flex items-center shadow-md">
        <button onClick={handleBack} className="mr-2">
          <ArrowLeft size={24} />
        </button>
        <h1 className="text-xl font-bold">확인</h1>
      </div>
      
      <div className="p-4 flex-1 bg-blue-50 flex flex-col items-center justify-center">
        <div className="bg-white rounded-lg shadow-md p-6 w-full max-w-md text-center">
          <div className="flex justify-center mb-4">
            <CheckCircle size={64} className="text-blue-600" />
          </div>
          
          <h2 className="text-2xl font-bold text-blue-800 mb-2">
            {currentScreen === 'createMatch' ? '경기 등록 완료!' : '경기 신청 완료!'}
          </h2>
          
          <p className="text-blue-700 mb-6">
            {currentScreen === 'createMatch' 
              ? '귀하의 경기가 성공적으로 등록되었습니다. 다른 참가자들이 곧 신청할 것입니다.'
              : '귀하의 참가 신청이 성공적으로 접수되었습니다. 주최자의 승인을 기다려주세요.'}
          </p>
          
          <button 
            className="w-full bg-blue-600 text-white p-3 rounded-lg font-bold mb-2"
            onClick={() => setCurrentScreen('map')}
          >
            홈으로 돌아가기
          </button>
          
          <button 
            className="w-full border border-blue-500 text-blue-600 p-3 rounded-lg font-bold"
            onClick={() => setCurrentScreen(currentScreen === 'createMatch' ? 'createMatch' : 'joinMatch')}
          >
            {currentScreen === 'createMatch' ? '다른 경기 등록하기' : '다른 경기 찾아보기'}
          </button>
        </div>
      </div>
    </div>
  );
  
  // 현재 화면에 따라 보여줄 컴포넌트 결정
  let CurrentScreenComponent;
  switch(currentScreen) {
    case 'map':
      CurrentScreenComponent = MapScreen;
      break;
    case 'regionDetail':
      CurrentScreenComponent = RegionDetailScreen;
      break;
    case 'matchOptions':
      CurrentScreenComponent = MatchOptionsScreen;
      break;
    case 'createMatch':
      CurrentScreenComponent = CreateMatchScreen;
      break;
    case 'joinMatch':
      CurrentScreenComponent = JoinMatchScreen;
      break;
    case 'confirmation':
      CurrentScreenComponent = ConfirmationScreen;
      break;
    default:
      CurrentScreenComponent = MapScreen;
  }
  
  return (
    <div className="h-screen max-w-md mx-auto overflow-hidden flex flex-col bg-blue-100 shadow-xl">
      <CurrentScreenComponent />
    </div>
  );
};

export default BasketballApp;
